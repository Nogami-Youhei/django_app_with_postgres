async function submitNewChoice() {
    const textBox = document.getElementById("input_choice_form");
    const choiceText = textBox.value,
        questionId = location.pathname.split('/')[2];

    const sendData = {
        'questionId': questionId,
        'choiceText': choiceText
    };

    // send api server
    // const endpoint = `${baseUrl}/register_choice/`
    const endpoint = 'http://192.168.32.174:8030/api/register_choice/'

    choiceApiRes = await fetch(
        endpoint, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(sendData),
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