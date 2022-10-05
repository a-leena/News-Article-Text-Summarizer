function getText(event) {
    var text = event.target.value;
    console.log(text);
    var count = text.length;
    document.getElementById("wordcount").innerHTML = count;
    var button = document.getElementById("summarize");
    var summary = document.getElementById("summary");
    if (text.length==0) {
        button.disabled = true;
        if (summary.innerHTML.length != 0) {
            var heading = document.getElementById("recentHeading")
            summary.innerHTML = "";
        }

    }
    else {
        button.disabled = false;
    }
}

function generateSummary() {
    let source = document.getElementById("input_text");

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