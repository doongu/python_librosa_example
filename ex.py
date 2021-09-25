import librosa
import soundfile as sf

def rosa(location):
    for (root, dirs, files) in os.walk(location):

        if len(files) > 0:
            for i in range(len(files)):
                loca = (root+  "/" + files[i]).replace("\\", "/")
                                # print(loca)
                audio, sr = librosa.load(loca, sr=16000)
                sf.write((root+  "/" +files[i][0] +"7" + files[i][1:]).replace("\\", "/"), audio, 16000, 'PCM_24')
                print("convert 완료")
