from urllib import request
import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
  ip_address = request.headers.get("x-forwarded-for")
  if not ip_address:
    ip_address = request.remote_addr
  return "<h1>Din IP-adress är: {}</h1>".format(ip_address)

if __name__ == "__main__":
  app.run(debug=True)