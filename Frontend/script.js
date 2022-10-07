function getText(event) {
    var text = event.target.value;
    console.log(text);
    var count = text.length;
    document.getElementById("wordcount").innerHTML = count;
    var submitButton = document.getElementById("summarize");
    var copyButton = document.getElementById("copy");
    var summary = document.getElementById("summary");
    if (text.length == 0) {
        submitButton.disabled = true;
        copyButton.disabled = true;
        summary.innerHTML = "";
    }
    else {
        submitButton.disabled = false;
        copyButton.disabled = false;
    }
}

function generateSummary() {
    source = document.getElementById("inputtext");
    console.log(source.value);

    let xhr = new XMLHttpRequest();
    let url = "http://localhost:8000";

    xhr.open("POST", url, true);

    xhr.setRequestHeader("Content-Type","application/json");

    xhr.onreadystatechange = function() {
        if(xhr.readyState === 4 && xhr.status === 200){
            parsed_data = JSON.parse(this.responseText);
            console.log(parsed_data['summary']);
            document.getElementById('summary').innerHTML = parsed_data['summary'];
        }
    };

    var data = JSON.stringify({"base_text": source.value});

    xhr.send(data);
}

function copyClipboard() {
    var copyText = document.getElementById("summary");
    console.log("something is running");
    navigator.clipboard.writeText(copyText.innerHTML);
    alert("Text copied!");
}