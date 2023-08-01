async function submitNewChoice() {
	const form = document.getElementById('add_item')
    const textBox = document.getElementById("input_choice_form");
    const choiceText = textBox.value
	
    // send api server
    // const endpoint = `${baseUrl}/register_choice/`
    const endPoint = 'http://localhost:8030/api/register_choice/'

    let choiceApiRes = await fetch(endPoint, {
        method: 'POST',
        body: new FormData(form)
    });

    const choiceRes = await choiceApiRes.json();

    if (choiceRes.status == 'success') {

        const choiceId = choiceRes['body']['choiceId'],
            choiceFieldset = document.getElementById("choice_fieldset");

        const inputElement = document.createElement('input'),
            labelElement = document.createElement('label'),
            divElement = document.createElement('div');

        divElement.setAttribute('class', "choice-area");

        inputElement.setAttribute('type', 'radio');
        inputElement.setAttribute('name', 'choice');
        inputElement.setAttribute('value', choiceId);
        inputElement.setAttribute('style', 'transform:scale(2.0);')
        inputElement.setAttribute('id', `choice${choiceId}`)
        divElement.appendChild(inputElement);

        labelElement.innerText = choiceText;
        labelElement.setAttribute('for', `choice${choiceId}`)
        divElement.appendChild(labelElement);
        choiceFieldset.appendChild(divElement);
        textBox.value = '';
    }
}