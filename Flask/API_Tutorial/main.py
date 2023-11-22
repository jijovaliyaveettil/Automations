from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

videos = {}



class Video(Resource):
    def get(self, video_id):
        return videos[video_id]
    
    def put(self):
        return
    
    def delete(self):
        
        

if __name__ == "__main__":
    app.run(debug=True)
