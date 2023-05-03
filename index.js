async function getData(symptoms) {
  try {
    const url = "http://localhost:6969/predict?symptoms=" + symptoms;
    let flaskAppData = await fetch(url).then((response) => {
      return response.json();
    });
    return flaskAppData.symptoms.final_prediction;
  } catch (err) {
    console.log(err);
    return "Error!";
  }
}

function diagnose() {
  if (selectedSymptomList.length!==0) {
    let resultDiv = document.getElementById("final_prediction");
    let symptoms = selectedSymptomList.toString();
    let resultCard = document.querySelector(".result");
    resultCard.style.display = "flex";
    getData(symptoms).then((data) => {
      resultDiv.innerText = data;
    });
  }
}

async function getSymptomsList() {
  try {
    const url = "http://localhost:6969/symptoms";
    let symptomsArray = await fetch(url).then((response) => {
      return response.json();
    });
    return symptomsArray;
  } catch (error) {
    console.log(error);
    return "Error!";
  }
}
let symptomList = [];
getSymptomsList().then((data) => {
  let dataList = document.querySelector("#data-list");
  symptomList = data;
  data.forEach((item) => {
    let newOption = document.createElement("option");
    newOption.setAttribute("value", item);
    dataList.append(newOption);
  });
});
let selectedSymptomList = [];
function addPill(event) {
  event.preventDefault();
  let input = document.getElementById("input");
  let addedSymptom = input.value;
  if (
    addedSymptom &&
    symptomList.includes(addedSymptom) &&
    !selectedSymptomList.includes(addedSymptom)
  ) {
    selectedSymptomList.push(addedSymptom);
    input.value = "";
    updatePills();
  } else if (selectedSymptomList.includes(addedSymptom)) {
    input.value = "";
    alert("Symptom Already Selected!");
  } else {
    input.value = "";
    alert("Select a valid Symptom!");
  }
}

function updatePills() {
  let symptomPillsContainer = document.querySelector("#symptomPillsContainer");
  symptomPillsContainer.innerHTML = "";
  selectedSymptomList.forEach((item) => {
    let newPill = document.createElement("div");
    newPill.className = "pill";
    newPill.innerText = item;
    symptomPillsContainer.append(newPill);
  });
}

function clearPills(event) {
  event.preventDefault();
  let input = document.getElementById("input");
  input.value = "";
  let symptomPillsContainer = document.querySelector("#symptomPillsContainer");
  symptomPillsContainer.innerHTML = "";
  selectedSymptomList = [];
  let resultCard = document.querySelector(".result");
  resultCard.style.display = "none";
}
