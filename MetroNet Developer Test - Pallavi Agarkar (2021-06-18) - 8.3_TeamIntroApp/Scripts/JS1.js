/// Validate the input fields and show message/alert if fields are blank
function Validate() {
    if (document.getElementById("txtName").value == "") {
        document.getElementById("txtName").focus();
        alert("Please enter valid Name");
        return false;
    }
    else if (document.getElementById("txtFunfact").value == "") {
        document.getElementById("txtFunfact").focus();
        alert("Please enter valid Funfact");
        return false;
    }
    return true;
}

/// Print the Name and Funfact on Console
function PrintInConsole() {
    if (Validate() === false)
        return;
    console.log("Team Intro:");
    console.log("Name: " + document.getElementById("txtName").value);
    console.log("Funfact: " + document.getElementById("txtFunfact").value);
    ShowDataOnFrm();
    ToggleState()
}

/// Show output on screen
function ShowDataOnFrm() {
    strName = document.getElementById("txtName").value;
    strfunFact = document.getElementById("txtFunfact").value

    document.getElementById("txtDataName").innerText = strName;
    document.getElementById("txtDataFunfact").innerText = strfunFact;
}
/// Toggle the form to accept input and show output on screen
function ToggleState() {
    var eFrm = document.getElementById("myFormId");
    var eDataFrm = document.getElementById("myDataId");

    if (eFrm.style.display === "none") {
        eFrm.style.display = "block";
        eDataFrm.style.display = "none";
    } else {
        eFrm.style.display = "none";
        eDataFrm.style.display = "block";

        ///Clear the input fields to accept new employee information
        document.getElementById("txtName").value = "";
        document.getElementById("txtFunfact").value = "";
    }

}