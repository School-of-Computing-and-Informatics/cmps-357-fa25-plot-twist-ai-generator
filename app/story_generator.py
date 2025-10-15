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
        used = set()

        # Helper to add a sentence if it's not a duplicate
        def add_sentence(s):
            if not s:
                return False
            key = s.strip()
            # Avoid exact duplicates
            if key in used:
                return False
            used.add(key)
            sentences.append(s)
            return True

        # Try to generate sentences
        for i in range(num_sentences * 2):  # allow some extra attempts
            if len(sentences) >= num_sentences:
                break
            try:
                if seed_words and len(sentences) == 0:
                    # Try to start with seed words but don't force exact repetition
                    sentence = None
                    try:
                        sentence = self.model.make_sentence_with_start(seed_words, strict=False)
                    except Exception:
                        sentence = None
                    # If markovify returns the exact seed text repeatedly, try a normal sentence
                    if sentence and seed_words.strip().lower() in sentence.strip().lower():
                        # Slightly vary the seed start by asking for a different follow-up
                        alt = self.model.make_sentence(tries=50)
                        if alt:
                            sentence = alt
                else:
                    sentence = self.model.make_sentence(tries=100)

                # If we couldn't get one, continue trying
                if not sentence:
                    continue

                # If sentence equals an obvious corpus line (exact match), try to slightly vary it
                if sentence.strip().endswith('.') and sentence.strip() in THRILLER_CORPUS:
                    # attempt small rephrasing by swapping a word or appending a short clause
                    words = sentence.split()
                    if len(words) > 3:
                        # swap two random words (not ideal but adds variation)
                        a, b = random.sample(range(len(words)), 2)
                        words[a], words[b] = words[b], words[a]
                        sentence = ' '.join(words)

                added = add_sentence(sentence)
                if not added:
                    # If duplicate, try again in the next loop
                    continue
            except (KeyError, markovify.text.ParamError):
                # If seed words don't work, generate without them
                sentence = self.model.make_sentence(tries=100)
                add_sentence(sentence)

        # If we couldn't generate enough unique sentences, pad with random corpus lines
        corpus_lines = [line.strip() for line in THRILLER_CORPUS.splitlines() if line.strip()]
        random.shuffle(corpus_lines)
        for line in corpus_lines:
            if len(sentences) >= num_sentences:
                break
            if line not in used:
                # don't add the exact same seed phrase if present
                add_sentence(line)

        # Final safety: if still short, repeat best-effort generated sentences (keep uniqueness where possible)
        if len(sentences) < num_sentences:
            attempts = 0
            while len(sentences) < num_sentences and attempts < 20:
                s = self.model.make_sentence(tries=100)
                add_sentence(s)
                attempts += 1

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
