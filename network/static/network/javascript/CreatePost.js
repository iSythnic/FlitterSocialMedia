document.addEventListener('DOMContentLoaded', ()=>{
    const createPostPopup = document.querySelector("#createPostPopup");

    document.querySelector("#create-post-btn").addEventListener('click', ()=>{
        createPostPopup.classList.remove('close');
        createPostPopup.classList.add('show');
    });

    document.querySelector('#popupCloseBtn').addEventListener('click', ()=>{
        createPostPopup.classList.remove('add');
        createPostPopup.classList.add('close');
    });

    document.querySelector("#createPostButton").addEventListener('click', ()=>{
        const form = document.querySelector("#createPostPopup-form");
        if (form.checkValidity())
        {

        }
    });
    document.querySelector("#post-fileupload").addEventListener('change', ()=>{
    })
})