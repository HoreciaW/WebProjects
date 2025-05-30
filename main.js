function buttonClicked() {
    console.log("Button Clicked");
    document.getElementById("text").innerHTML="Added to Cart";
    var customText = document.getElementsByClassName("my-input");
    var results = document.getElementById("course")
    results.innerHTML = customText[0].value;
}

var btn = document.getElementById("go-button");

btn.addEventListener("click",buttonClicked);




/*
function getPhraseLength(phrase,another) {
        var l =phrase.length;
        return l;

}
 
var p1= "This is a slightly longer sentence";
var p2 = "This is a  shorter sentence." ;
var thisLength=getPhraseLength(p1,p2);
console.log(thisLength);


/*var Courses = ["Calculus and Vectors","Chemistry","Physics","English"]; //Array//

console.log(Courses); //array.pop removes  last item from list//
console.log("We no longer offer ",Courses.pop());
Courses.push("Advanced Functions") //Adds to list//
*/



// Methods use () at the end and variables like .length only does not need the()//






// Hyphens cannot be used in fucntion names or varibles but it is a must in css
/* Multilined comment*/
// Single lined comment //
//document.write();//

/*var welcome_message="Welcome to Source e-learning !";
var myAge=18; //Integer//
var my_Age=18.3; //Float//
var myName;
alert(welcome_message);
console.log("This is a log !");
console.log("My name is" + myName);
myAge+=2;
var horecia=true;
horecia==true
horecia=="true"

var isPremiumUser=true;
if(isPremiumUser==true) {
    console.log("Thanks for being a loyal customer")
}else{
    console.log(|"You should subscribe to our premium service")
}
var myAge=28;
if (myAge<1){
    console.log("You are a baby")
}else if(myAge<3){
    "You are a toddler"
}else if(myAge<10){
    console.log("You're a big kid")
}else if(myAge<40){
    console.log("You are an adult.")
}else if(myAge<=19){
    console.log("You are a teenager")
}else{
    console.log("You must beold,you're not in out records.")
}


for(var i=0; 0; i<10; 1++){
    console.log("Current i value is", i);
}

function myFunction() {
    console.log("My name is nick")
}
myFunction();
function printName(name,age){
    console.log("Hello,",name,". You are", age);
}
printName("Nick",19);
printName("Charcles",20);*/