function loadMedicalHisotryDetails(medicalHistoryId) {
    console.log(medicalHistoryId);
    var diseaseName = document.getElementById("diseaseName");
    var diseaseSymptoms = document.getElementById("diseaseSymptoms");
    var doctorName = document.getElementById("doctorName");
    var historyDescription = document.getElementById("historyDescription");
    var hospitalName = document.getElementById("hospitalName");
    var diseaseDate = document.getElementById("diseaseDate");
    var birthDate = document.getElementById("birthDate");
    var userHeight = document.getElementById("userHeight");
    var userWeight = document.getElementById("userWeight");
    var userAge = document.getElementById("userAge");
    var userAllergy = document.getElementById("userAllergy");
    var userDisability = document.getElementById("userDisability");
    var diseaseInherit = document.getElementById("diseaseInherit");
    var userBloodGroup = document.getElementById("userBloodGroup");


    var ajax = new XMLHttpRequest();
    ajax.onreadystatechange = function () {
        if (ajax.readyState === 4) {
            console.log(ajax.responseText);
            var jsn = JSON.parse(ajax.responseText);
            if (jsn.length !== 0) {
                diseaseName.innerHTML = jsn[0].medicalhistory_disease_name;
                diseaseDate.innerHTML = jsn[0].medicalhistory_date;
                diseaseInherit.innerHTML = jsn[0].medicalhistory_inherited;
                birthDate.innerHTML = jsn[0].medicalhistory_birth_date;
                doctorName.innerHTML = jsn[0].medicalhistory_doctor_name;
                diseaseSymptoms.innerHTML = jsn[0].medicalhistory_symptoms;
                historyDescription.innerHTML = jsn[0].medicalhistory_description;
                userAge.innerHTML = jsn[0].medicalhistory_age;
                userAllergy.innerHTML = jsn[0].medicalhistory_allergy;
                userBloodGroup.innerHTML = jsn[0].medicalhistory_blood_group;
                userDisability.innerHTML = jsn[0].medicalhistory_disability;
                userHeight.innerHTML = jsn[0].medicalhistory_height;
                userWeight.innerHTML = jsn[0].medicalhistory_weight;
                hospitalName.innerHTML = jsn[0].medicalhistory_hospital_name;

            }
        }
    };
    ajax.open("get", "/user/ajax_view_medicalhistory?medicalHistoryId=" + medicalHistoryId, true);
    ajax.send();
}
function loadMedicalHisotryDetail(medicalHistoryId) {
    console.log(medicalHistoryId);
    var diseaseName = document.getElementById("diseaseName");
    var diseaseSymptoms = document.getElementById("diseaseSymptoms");
    var doctorName = document.getElementById("doctorName");
    var historyDescription = document.getElementById("historyDescription");
    var hospitalName = document.getElementById("hospitalName");
    var diseaseDate = document.getElementById("diseaseDate");
    var birthDate = document.getElementById("birthDate");
    var userHeight = document.getElementById("userHeight");
    var userWeight = document.getElementById("userWeight");
    var userAge = document.getElementById("userAge");
    var userAllergy = document.getElementById("userAllergy");
    var userDisability = document.getElementById("userDisability");
    var diseaseInherit = document.getElementById("diseaseInherit");
    var userBloodGroup = document.getElementById("userBloodGroup");


    var ajax = new XMLHttpRequest();
    ajax.onreadystatechange = function () {
        if (ajax.readyState === 4) {
            console.log(ajax.responseText);
            var jsn = JSON.parse(ajax.responseText);
            if (jsn.length !== 0) {
                diseaseName.innerHTML = jsn[0].medicalhistory_disease_name;
                diseaseDate.innerHTML = jsn[0].medicalhistory_date;
                diseaseInherit.innerHTML = jsn[0].medicalhistory_inherited;
                birthDate.innerHTML = jsn[0].medicalhistory_birth_date;
                doctorName.innerHTML = jsn[0].medicalhistory_doctor_name;
                diseaseSymptoms.innerHTML = jsn[0].medicalhistory_symptoms;
                historyDescription.innerHTML = jsn[0].medicalhistory_description;
                userAge.innerHTML = jsn[0].medicalhistory_age;
                userAllergy.innerHTML = jsn[0].medicalhistory_allergy;
                userBloodGroup.innerHTML = jsn[0].medicalhistory_blood_group;
                userDisability.innerHTML = jsn[0].medicalhistory_disability;
                userHeight.innerHTML = jsn[0].medicalhistory_height;
                userWeight.innerHTML = jsn[0].medicalhistory_weight;
                hospitalName.innerHTML = jsn[0].medicalhistory_hospital_name;

            }
        }
    };
    ajax.open("get", "/admin/ajax_view_medicalhistory?medicalHistoryId=" + medicalHistoryId, true);
    ajax.send();
}

