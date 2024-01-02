import nltk
import tiktoken
nltk.download('punkt')

class DocumentSegmenter():
    def __init__(self, document, token_limit=2800, max_token_limit=3500, model="gpt-3.5-turbo-1106"):
        self.document = document
        self.token_limit = token_limit
        self.max_token_limit = max_token_limit
        self.tokenizer = tiktoken.encoding_for_model(model)
        self.sentences = nltk.tokenize.sent_tokenize(document)

    def segment_document(self):
        """
        Break the document into segments of text.
        """
        segments = []
        current_segment = ''
        for sentence in self.sentences:
            if len(self.tokenizer.encode(current_segment + sentence)) <= self.token_limit:
                current_segment += sentence + ' '
            else:
                if current_segment:
                    segments.append(current_segment.strip())
                current_segment = sentence + ' '

        if current_segment:
            segments.append(current_segment.strip())

        # Adjust segment boundaries if necessary
        self.adjust_segments(segments)

        return segments

    def adjust_segments(self, segments):
        """
        Adjust segment boundaries if necessary.
        """
        for i in range(len(segments) - 1):
            while len(self.tokenizer.encode(segments[i])) > self.max_token_limit:
                # Move the last sentence to the next segment
                last_sentence = segments[i].split('. ')[-1]
                segments[i] = segments[i].replace(last_sentence, '').strip()
                segments[i + 1] = last_sentence + ' ' + segments[i + 1]
