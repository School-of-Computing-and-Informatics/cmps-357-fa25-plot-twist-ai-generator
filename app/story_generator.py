"""
Story generator module using Markov chains
"""
import markovify
import random

# Sample thriller corpus for training the Markov chain
THRILLER_CORPUS = """
The dark figure moved silently through the shadows. A mysterious stranger appeared at the door.
The detective knew something was wrong. The old mansion held terrible secrets.
She heard footsteps behind her in the empty corridor. The lights flickered and went out suddenly.
A scream echoed through the night. Nobody could be trusted anymore.
The clock struck midnight as the door creaked open. Danger lurked around every corner.
He discovered the hidden room behind the bookshelf. The truth was more terrifying than anyone imagined.
The phone rang at 3 AM with a threatening message. Someone was watching from the darkness.
The evidence pointed to an impossible conclusion. Time was running out to solve the mystery.
She found the cryptic note left on her desk. The killer was closer than they thought.
The abandoned warehouse concealed a deadly secret. Fear gripped her heart as she ventured deeper.
A mysterious package arrived with no return address. The past had come back to haunt them.
The witness disappeared without a trace. Something sinister was happening in this quiet town.
He recognized the face from his nightmares. The investigation took a dark turn.
Strange symbols were carved into the walls. No one knew who would be next.
The storm isolated them in the remote cabin. Trust no one, suspect everyone.
A shadowy organization pulled the strings. The conspiracy went deeper than imagined.
Blood was found at the scene. The victim's last words were a cryptic warning.
She decoded the message but it was too late. Evil walked among them undetected.
The footprints led to a shocking revelation. Darkness consumed the city streets.
He uncovered a web of lies and deception. The thriller reached its terrifying climax.
"""

class StoryGenerator:
    """Generate thriller stories using Markov chains"""
    
    def __init__(self):
        self.model = None
        self.train()
    
    def train(self):
        """Train the Markov chain model on the thriller corpus"""
        self.model = markovify.Text(THRILLER_CORPUS, state_size=2)
    
    def generate_story(self, num_sentences=10, seed_words=None):
        """
        Generate a thriller story
        
        Args:
            num_sentences: Number of sentences to generate
            seed_words: Optional seed words to start the story
            
        Returns:
            Generated story text
        """
        if not self.model:
            self.train()
        
        sentences = []
        
        # Try to generate sentences
        for _ in range(num_sentences):
            try:
                if seed_words and len(sentences) == 0:
                    # Try to start with seed words
                    sentence = self.model.make_sentence_with_start(seed_words, strict=False)
                else:
                    sentence = self.model.make_sentence(tries=100)
                
                if sentence:
                    sentences.append(sentence)
            except (KeyError, markovify.text.ParamError):
                # If seed words don't work, generate without them
                sentence = self.model.make_sentence(tries=100)
                if sentence:
                    sentences.append(sentence)
        
        # If we couldn't generate enough sentences, pad with some extras
        while len(sentences) < num_sentences:
            sentence = self.model.make_sentence(tries=100)
            if sentence:
                sentences.append(sentence)
        
        return ' '.join(sentences[:num_sentences])
    
    def generate_twist(self):
        """Generate a plot twist"""
        twists = [
            "But then, a shocking revelation changed everything.",
            "Suddenly, the truth became crystal clear.",
            "In that moment, everything made terrifying sense.",
            "The real villain had been hiding in plain sight.",
            "What seemed like the end was only the beginning.",
            "The detective realized they had been wrong all along.",
            "A final clue emerged from the shadows.",
            "The twist no one saw coming finally revealed itself."
        ]
        return random.choice(twists)
