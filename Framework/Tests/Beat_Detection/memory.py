from concurrent.futures import ThreadPoolExecutor
import threading
import librosa
import pandas as pd

class AudioFileHandler:
    """
    A class that handles audio file operations and beat detection.

    Attributes:
        file_path (str): The path to the audio file.

    Methods:
        __init__(file_path): Initializes the AudioFileHandler object.
        detect_beats(): Detects beats in the audio file and returns the time positions.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.y, self.sr = librosa.load(file_path, sr=None)

    def detect_beats(self):
        """
        Detects beats in the audio file.

        Returns:
            list: A list of time positions (in seconds) where beats occur.
        """
        tempo, beats = librosa.beat.beat_track(y=self.y, sr=self.sr)
        return librosa.frames_to_time(beats, sr=self.sr)

# Modify the beat_detection function to support threading
def beat_detection(input_file, repetitions, num_threads):
    """
    Perform beat detection on an audio file using multiple threads.

    Args:
        input_file (str): The path to the input audio file.
        repetitions (int): The number of times to repeat the beat detection process.
        num_threads (int): The number of threads to use for parallel processing.

    Returns:
        None

    Saves:
        - accumulated_beat_times.csv: A CSV file containing the accumulated beat times.

    """
    all_beats = []
    lock = threading.Lock()

    def process_iteration(iteration):
        audio_handler = AudioFileHandler(input_file)
        beat_times = audio_handler.detect_beats()

        with lock:
            for beat_time in beat_times:
                all_beats.append({'iteration': iteration, 'beat_time': beat_time})

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in range(repetitions):
            executor.submit(process_iteration, i+1)

    df = pd.DataFrame(all_beats)
    df.to_csv('accumulated_beat_times.csv', index=False)

# Adjust the parameters as needed
INPUT_FILE = 'Popia.ogg'
REPETITIONS = 400
NUM_THREADS = 12  # Adjust based on your system's capability
beat_detection(INPUT_FILE, REPETITIONS, NUM_THREADS)
