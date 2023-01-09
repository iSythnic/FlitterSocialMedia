document.querySelectorAll('.read-more-link').addEventListener('click', (event) => {
    event.preventDefault();
    console.log("123");
    const line = document.querySelector(event.target.dataset.descID);
    line.classList.remove("active");
    event.target.remove();
})