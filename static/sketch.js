const { ml5 } = window;
const classifier = ml5.imageClassifier("MobileNet", console.log);
// Use the link below instead of "MobileNet" to turn Seefood into Hotdog or not.
// "https://teachablemachine.withgoogle.com/models/-JrVsmzr/model.json"

const result = document.getElementById("result");

async function classifyImage() {
  const results = await classifier.classify(image);
  result.innerText = results[0].label;
}

function Apply(){
  
  var fileInput = document.getElementById("myfileinput");

  // files is a FileList object (similar to NodeList)
  var files = fileInput.files;
  var file;
  
  // loop through files
  for (var i = 0; i < files.length; i++) {
  
      // get item
      file = files.item(i);
      //or
      file = files[i];
  
      alert(file.name);
  }
  

}


  
  
  //console.log(files[0]);
  //image.src = URL.createObjectURL(files[0]);
  //console.log(image.src);
  //setTimeout(classifyImage, 50);

