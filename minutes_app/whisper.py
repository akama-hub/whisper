from faster_whisper import WhisperModel

class WhisperModelWrapper:
    # GPUを使用するか
    GPU_flag = 0

    def __init__(self):
        self.model_size_or_path = "large-v3"
        if self.GPU_flag == 1:
            # GPUを使用する設定
            self.model = WhisperModel(
                self.model_size_or_path, device="cuda", compute_type="float16"
            )
        else:
            # CPUのみの設定
            self.model = WhisperModel(
                self.model_size_or_path, device="cpu", compute_type="int8"
            )

    def transcribe(self, audio):
        # 出力からタイムスタンプを消す
        segments, _ = self.model.transcribe(
            audio=audio, beam_size=3, language="ja", without_timestamps=True 
        )
        return segments