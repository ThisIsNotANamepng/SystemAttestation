from flask import Flask, request, jsonify
import sqlite3
import signature_getter

def get_signature_database(system, package, version):

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    print("SELECT * FROM hashes WHERE system = '"+system+"' AND package = '"+package+"' AND version = '"+version+"';")
    cursor.execute("SELECT * FROM hashes WHERE system = '"+system+"' AND package = '"+package+"' AND version = '"+version+"';")
    data = cursor.fetchall()
    conn.close()

    if data:
        return data[0]
    else:
        return "none"

def exists(system, package, version):
    # This is the def the page calls, it uses get_signature
    hash = get_signature_database(system, package, version)

    if not hash:
        # hash isn't in the database, now need to checks with the container to see if it has it, 
        # if not we return no package found
        # if yes we put the package in the database and return it
        a=1

def get_signature_image(system, package):
    # This gets the signature from the image fleet, used if the signature isn't in the database
    return signature_getter.signature(package, system)


app = Flask(__name__)

@app.route('/signature', methods=['GET'])
def route_signature():

    system = request.args.get('system')
    package = request.args.get('package')
    version = request.args.get('version')

    if not package or not version or not system:
        print(package, version, system)
        return "Missing package or version"
    
    signature = get_signature_database(package, version, system)

    if signature == "none":
        # The signature isn't in the database, need to get it from the image fleet
        signature = get_signature_image(system, package)

    print(signature)
    return signature

@app.route('/exists', methods=['GET'])
def route_exists():

    try:
        system = request.args.get('system')
        package = request.args.get('package')
        version = request.args.get('version')

        if system == None or package == None or version == None:
            return "Missing data"

        print(system, package, version)
    except:
        return 'Failed'
    
    hash = get_signature(system, package, version)

    if not hash:
        return 'Does not exist'

    return hash

if __name__ == '__main__':
    app.run(debug=True)
