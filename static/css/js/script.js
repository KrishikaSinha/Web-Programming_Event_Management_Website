function validateForm() {
    let name = document.getElementsByName("name")[0].value;
    let email = document.getElementsByName("email")[0].value;

    if (name === "" || email === "") {
        alert("All fields required!");
        return false;
    }
    return true;
}