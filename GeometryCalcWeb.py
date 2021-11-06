# SENG3110 Software Testing
# 
# Project: Geometry Calculator Web App
#
# Sample Code for the Python Flask Web App Implementation of the Geometry Calculator
#
# Author: Joe Axberg
# Editor: Sarah Fox
# Orig Date: 9/22/2021
#
# imports
from flask import Flask, request, render_template, redirect, url_for
import cylinder #makes the code in cylinder.py available to be used in the frontend for user to see
import sphere # makes methods from sphere object available
import cone # makes methods from cone object available

#flask plumbing
app = Flask(__name__)

#flask route for the index page
#uses html template for user selection
@app.route("/", methods = ["GET", "POST"]) #this makes the homepage render
def mainForm():
   if request.method == "POST":
      ## This determines which selection the user made
      #sphere = request.form.get("sphere")
      #cylinder = request.form.get("cylinder")
      #cone = request.form.get("cone")
      selection = request.form['shape'] 
      print("Selection was: ", sphere, cylinder, cone) #prints to command line for trouble shooting
      if selection == "sphere":
         print("User selected sphere") #prints to command line for trouble shooting
         return redirect(url_for('sphereForm'))
      if selection == "cylinder":
         print("User selected cylinder") #prints to command line for trouble shooting
         return redirect(url_for('cylinderForm'))
      if selection == "cone":
         print("User selected cone")
         return redirect(url_for('coneForm'))
   return render_template("index.html")

#flask route for the cylinder calculations page
@app.route("/cylinder", methods = ["GET", "POST"])
def cylinderForm():
   if request.method == "POST":
       # getting input with name = fname in HTML form
       radius = request.form.get("rad")
       # getting input with name = lname in HTML form 
       height = request.form.get("hgt") 
       vol = cylinder.volume(int(radius), int(height))
       lat = cylinder.lateral(int(radius), int(height))
       cylSurf = cylinder.surfaceArea(int(radius), int(height))
       base = cylinder.base(int(radius))
       return render_template("cylinder-results.html", radius = radius, height = height, vol = vol, lat = lat, cylSurf = cylSurf, base = base)
   return render_template("cylinder.html")

#flask route for the sphere calculations page
@app.route("/sphere", methods = ["GET", "POST"])
def sphereForm():
   if request.method == "POST":
       # getting input with name = fname in HTML form
       radius = request.form.get("rad")
       vol = sphere.volume(int(radius))
       surf = sphere.surfaceArea(int(radius))
       #return "User entered: Radius "+ str(radius) + ". <p>The Volume is: " + str(vol) + "and the Surface Area is: " + str(surf) + ""
       return render_template("sphere-result.html", vol = vol, surf=surf, radius = radius)
   return render_template("sphere.html")

#flask route for the cone calculations page
@app.route("/cone", methods = ["GET", "POST"])
def coneForm():
   if request.method == "POST":
       # getting input with name = fname in HTML form
       radius = request.form.get("rad")
       height = request.form.get("hgt") 
       slant = cone.slant(int(radius), int(height))
       surf = cone.surface(int(radius), int(height))
       return render_template("cone-results.html", radius = radius, height = height, slant = slant, surf = surf)
   return render_template("cone.html")

#more code here for the rest of the calculators: sphere, cube, etc.
  
if __name__=='__main__':   #more flask plumbing so the environment starts correctly
   app.run(host='0.0.0.0')
