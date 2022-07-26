def create_youtube_video(title,descripotion):
	utubevid = {"title":
	title,"descripotion":descripotion,"likes":0,"dis likes":0,"comments":{}}
	return utubevid
	
def like(utubevid):
		if "likes" in utubevid:
			utubevid["likes"]+=1
			return utubevid

def dislike(utubevid):
	if"dislikes" in utubevid:
		utubevid["dislikes"]+=1
		return utubevid

def add_comment(utubevid,username,comments_text):
	utubevid["comments"][username] = comments_text
	return utubevid
you = create_youtube_video("are","sdjl")
for i in range(495):
	like(you)
	dislike(you)
	add_comment(you,"zxi","psdiuo")