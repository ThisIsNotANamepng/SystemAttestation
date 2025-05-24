from flask import Flask, request, jsonify
import sqlite3
import generator 

def get_signature_database(system, package, version):

    conn = sqlite3.connect('../database.db')
    cursor = conn.cursor()
    print("SELECT * FROM "+system+" WHERE package = '"+package+"' AND version = '"+version+"';")
    cursor.execute("SELECT * FROM "+system+" WHERE package = '"+package+"' AND version = '"+version+"';")
    data = cursor.fetchall()
    conn.close()

    print(data)

    if data:
        return data[0]
    else:
        return "none"

def check_if_package_in_database(system, package, version):
    # This is the def the page calls, it uses get_signature
    hash = get_signature_database(system, package, version)

    if not hash:
        # hash isn't in the database, now need to checks with the container to see if it has it, 
        # if not we return no package found
        # if yes we put the package in the database and return it
        a=1

app = Flask(__name__)

@app.route('/signature', methods=['GET'])
def route_signature():

    system = request.args.get('system')
    package = request.args.get('package')
    version = request.args.get('version')

    if not package or not version or not system:
        print(package, version, system)
        return "Missing package or version"
    
    signature = get_signature_database(system, package, version)

    if signature == "none":
        # The signature isn't in the database, need to get it from the image fleet

        if generator.package_safety(system, package):
            generator.new_package(system, package)
        else:
            return "Invalid package"
        
        signature = get_signature_database(system, package, version)

    print(signature)
    return signature[2]

@app.route('/batch', methods=['GET'])
def batch():
    # Takes a number of packages in one dump
    print()


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
    
    hash = get_signature_database(system, package, version)

    if not hash:
        return 'Does not exist'

    return hash

if __name__ == '__main__':
    app.run(debug=True)
