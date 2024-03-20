# Faster-whisper
WhisperAPI を利用せずにローカル環境でリアルタイム文字起こし

## 環境
Python で CUDA が利用できること

## モデル
Whisper modelの初期化時にmodel_sizeではなく、ローカルに保存したmodelのパスを指定すればオフラインで動作する

## 参考
+ [faster-whisper](https://github.com/SYSTRAN/faster-whisper)
+ [本家Whisper](https://github.com/openai/whisper)
+ [[ローカル環境] faster-whisperを利用してリアルタイム文字起こしに挑戦](https://qiita.com/reriiasu/items/920227cf604dfb8b7949)