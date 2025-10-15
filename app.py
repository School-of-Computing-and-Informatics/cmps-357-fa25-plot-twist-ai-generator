"""
PlotTwist - AI-assisted thriller story generator
Main Flask application
"""
from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import json
import os
from app.story_generator import StoryGenerator

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'

# Initialize story generator
generator = StoryGenerator()

# Simple in-memory storage for stories (in production, use a database)
stories = {}
next_id = 1

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """Generate a new thriller story"""
    global next_id
    
    data = request.get_json()
    num_sentences = int(data.get('num_sentences', 10))
    seed_words = data.get('seed_words', '').strip()
    include_twist = data.get('include_twist', True)
    
    # Generate the story
    if seed_words:
        story_text = generator.generate_story(num_sentences=num_sentences, seed_words=seed_words)
    else:
        story_text = generator.generate_story(num_sentences=num_sentences)
    
    # Add a plot twist if requested
    if include_twist:
        twist = generator.generate_twist()
        story_text = f"{story_text} {twist}"
    
    # Save the story
    story_id = next_id
    next_id += 1
    
    stories[story_id] = {
        'id': story_id,
        'text': story_text,
        'created_at': datetime.now().isoformat(),
        'title': f"Thriller Story #{story_id}"
    }
    
    return jsonify({
        'success': True,
        'story_id': story_id,
        'text': story_text
    })

@app.route('/stories')
def list_stories():
    """List all saved stories"""
    return render_template('stories.html', stories=stories.values())

@app.route('/story/<int:story_id>')
def view_story(story_id):
    """View a specific story"""
    story = stories.get(story_id)
    if not story:
        return "Story not found", 404
    return render_template('story.html', story=story)

@app.route('/story/<int:story_id>/edit', methods=['GET', 'POST'])
def edit_story(story_id):
    """Edit a story"""
    story = stories.get(story_id)
    if not story:
        return "Story not found", 404
    
    if request.method == 'POST':
        data = request.get_json()
        story['text'] = data.get('text', story['text'])
        story['title'] = data.get('title', story['title'])
        return jsonify({'success': True})
    
    return render_template('edit.html', story=story)

@app.route('/story/<int:story_id>/delete', methods=['POST'])
def delete_story(story_id):
    """Delete a story"""
    if story_id in stories:
        del stories[story_id]
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'Story not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
