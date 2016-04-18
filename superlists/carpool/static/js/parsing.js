var debugging = false;
var splitChar = "_";

// A class used to parse objects from a SQL Lite Database in the Python DjangoFramework
function PythonDatabaseObjectParser (){};

// Takes a single object and returns it as an array of parameters (removes object header)
PythonDatabaseObjectParser.prototype.parseObjectAsArray = function(objectAsText, obectHeaderString) {
    // Removes the header
    objectAsText = objectAsText.replace(obectHeaderString + ": ", "");
    // And the chevrons
    objectAsText = objectAsText.replace("<", "");
    objectAsText = objectAsText.replace(">", "");

    var objectAsArray = objectAsText.split(splitChar);

    return objectAsArray;
};

// Parses a single string into an array of strings: still in the SQL Lite database format
PythonDatabaseObjectParser.prototype.parseStringAsStringArray = function(objectArrayAsText) {
    objectArrayAsText = objectArrayAsText.replace("]", "");
    objectArrayAsText = objectArrayAsText.replace("[", "");
    objectArrayAsText = objectArrayAsText.replace(/>,/g, ">_");
    return objectArrayAsText.split(splitChar + " ");

}

// Parses a single string in the SQL Lite database format into a matrix of strings (2D Array)
PythonDatabaseObjectParser.prototype.parseObjectArrayAsStringMatrix = function(
  objectArrayAsTextArray,
  objectHeaderAsString) {

  console.log(objectArrayAsTextArray)
  objectArrayAsTextArray = this.replaceEscapeCharacters(objectArrayAsTextArray);

  var allObjectsAsStringArrays = [];

  var allObjectsAsStrings = this.parseStringAsStringArray(objectArrayAsTextArray);

  for (var i = 0; i < allObjectsAsStrings.length; i++) {
    allObjectsAsStringArrays.push(this.parseObjectAsArray(allObjectsAsStrings[i], objectHeaderAsString));
  }

  return allObjectsAsStringArrays;

}

// Used to replace special characters in the SQL Lite string (preprocessing function)
PythonDatabaseObjectParser.prototype.replaceEscapeCharacters = function(objectsAsString) {
    objectsAsString = objectsAsString.replace(/&lt/g, "<");
    objectsAsString = objectsAsString.replace(/&gt/g, ">");
    objectsAsString = objectsAsString.replace(/\n/g, "");
    objectsAsString = objectsAsString.replace(/;/g, "");
    return objectsAsString;
}


function Route (start, stop) {
  this.start = start;
  this.stop = stop;
}

Route.parseFromString = function (routeAsString) {
  var parameters = routeAsString.split("to");
  var startString = parameters[0];
  var stopString = parameters[1];

  var start = JSON.parse(startString);
  var stop = JSON.parse(stopString);

  return new Route (start, stop);
}

// Used to represent a user in JavaScript
function User (lastName, firstName, start, end, date, route) {
  this.firstName = firstName;
  this.lastName = lastName;
  this.start = start;
  this.end = end;
  this.date = date;
  this.route = route
}

// Static function: creates a user from a string array of length 5
User.parseFromStringArray = function (stringArray) {
    // Assumes a particular ordering
    return new User (
        stringArray[0].trim(),
        stringArray[1].trim(),
        stringArray[2].trim(),
        stringArray[3].trim(),
        stringArray[4].trim(),
        Route.parseFromString(stringArray[5])
    );
}

// Static function: Takes a 2D array of strings and parses as an array of users
// intended to be used in conjunction with: parseObjectArrayAsStringMatrix
User.parseFromStringArrayMatrix = function (stringMatrix) {
  users = [];
  for (var i = 0; i < stringMatrix.length; i++) {
      users.push(User.parseFromStringArray(stringMatrix[i]));
  }
  return users;
}

if (debugging) {
  console.log(Route.parseFromString("{\"Lat\": 47.2868352, \"Lng\": -120.2126138}to{\"Lat\": 41.8935085, \"Lng\": 12.4825526}"));
}
