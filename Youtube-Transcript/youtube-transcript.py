from youtube_transcript_api import YouTubeTranscriptApi as yta
import re

vid_id="Vzh5guYUyvM&list=PLq-Gm0yRYwThGmlypvSFQ-kT2rPaXKAZ5&index=1"

data=yta.get_transcript(vid_id)

transcript=''
for value in data:
    for key,val in value.items():
        if key=='text':
            transcript+=val
        
l = transcript.splitlines()
final_trans="".join(l)

file=open("sample.txt",'w')
file.write(final_trans)
file.close()




    
