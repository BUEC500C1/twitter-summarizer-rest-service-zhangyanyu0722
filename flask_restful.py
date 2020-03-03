from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from tweepy_get import tweepy_get
from image2video import image_to_video
from queue_sys import queue_1
import multiprocessing, time, threading, queue, os

app = Flask(__name__)
api = Api(app)

twitter_names = {
    'BU_Tweets': {'twitter_name': 'BU_Tweets'},
    'BU_ece': {'twitter_name': 'BU_ece'},
    'BostonDynamics': {'twitter_name': 'BostonDynamics'},
    'BBCWorld': {'twitter_name': 'BBCWorld'},
    'WHO': {'twitter_name': 'WHO'},
    'TIME': {'twitter_name': 'TIME'},
    'celtics': {'twitter_name': 'celtics'},
    'nytimes': {'twitter_name': 'nytimes'},
    'washingtonpost': {'twitter_name': 'washingtonpost'},
    'BillGates': {'twitter_name': 'BillGates'},
}


def abort_if_todo_doesnt_exist(t_id):
    if t_id not in twitter_names:
        abort(404, message="Todo {} doesn't exist".format(t_id))


parser = reqparse.RequestParser()
parser.add_argument('twitter_name', type=str)


class Update_Delete_Keyword(Resource):
    def get(self, t_id):              
        abort_if_todo_doesnt_exist(t_id)
        print(twitter_names[t_id]['twitter_name'])
        keyword = twitter_names[t_id]['twitter_name']
        tweepy_get(keyword)
        image_to_video(keyword)
        return twitter_names[t_id]

    def delete(self, t_id):        
        abort_if_todo_doesnt_exist(t_id)
        del twitter_names[t_id]
        return 'delete success', 204

    def post(self, t_id):            
        abort_if_todo_doesnt_exist(t_id)
        return twitter_names, 201

    def put(self, t_id):          
        args = parser.parse_args()
        twitter_name = {'twitter_name': args['twitter_name']}
        twitter_names[t_id] = twitter_name
        return twitter_names, 201

api.add_resource(Update_Delete_Keyword, '/twitter/<t_id>')

if __name__ == '__main__':
    app.run(debug=True)


