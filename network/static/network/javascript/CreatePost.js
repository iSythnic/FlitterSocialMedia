
document.addEventListener('DOMContentLoaded', ()=>{
    const createPostPopup = document.querySelector("#createPostPopup");
    const body = document.querySelector('body');

    document.querySelector("#create-post-btn").addEventListener('click', ()=>{
        createPostPopup.classList.remove('close');
        createPostPopup.classList.add('show');
        body.style.overflowY = 'hidden';
    });

    document.querySelector('#popupCloseBtn').addEventListener('click', ()=>{
        createPostPopup.classList.remove('add');
        createPostPopup.classList.add('close');
        document.querySelector("#createPostPopup-form").reset();
        document.querySelector("#createPostPopup-image-display").innerHTML = '';
        body.style.overflowY = 'scroll';
    });

    document.querySelector("#createPostPopup-form").addEventListener('submit', async (event) => {
        event.preventDefault();
        if (event.target.checkValidity())
        {
            const payload = new FormData(event.target);
            const csrf = [...payload][0][1];
            const response = await fetch('http://127.0.0.1:8000/share', {
                credentials: "same-origin",
                mode: 'same-origin',
                method: "POST",
                headers: {
                    "X-CSRFToken": csrf
                },
                body: payload
            });
            if (!response.ok)
                console.log(await response.json().error);
        }
    });

    document.querySelector("#post-fileupload").addEventListener('change', (event)=>{
        const imageContainer = document.querySelector('#createPostPopup-image-display');
        imageContainer.innerHTML = `
            <img src="${URL.createObjectURL(event.target.files[0])}" class="createPostImagePreview" alt="image"></img>
        `;
    });
})