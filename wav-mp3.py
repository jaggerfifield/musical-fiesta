import os

def setup(export):
    os.system("CLS")
    info("Looking for output folder . . .")
    
    for file in os.listdir():
        if(file == export):
            error("Found file called " + export + ". Will not overwrite.")
            exit()
    info("Making output folder . . .")
    os.system("MKDIR " + export)

def run(export):
    
    count = 0

    for file in os.listdir():
        if(file[-3:] == 'wav'):
            count = count + 1
            
            command = "ffmpeg -r 10 -i \"./" + str(file) + "\" \"" + str(file.rstrip(".wav")) + ".mp3\""
            
            info("Trying : " + command)
            os.system(command)
            
            info("Moving mp3 file to " + export)
            os.system("MV \"" + str(file.rstrip(".wav")) + ".mp3\" ./" + export)
    info("Found " + str(count) + " files")

def info(text):
    print("\x1b[38;2;35;176;237m" + "[Infos]" + "\x1b[0m : " + text)
    
def error(text):
    print("\x1b[38;2;237;49;35m" + "[Error]" + "\x1b[0m : " + text)

def main():
    export = "mp3"
    setup(export)
    run(export)
    
main()
