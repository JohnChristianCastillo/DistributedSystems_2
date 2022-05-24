# this file is purely for development
from client.project.app import app

if __name__ == '__main__':
    # 0.0.0.0 is convention IP-address that will enable connection for all
    # network interfaces and is something that we want to execute web-based
    # services in Docker containers, so it will be easier to expose the connection
    # from the container to our local host
    app.run(host='0.0.0.0', port=5001, debug=True)