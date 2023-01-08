loadContent = async () =>{
    const contentarea = document.querySelector("#feed-container");
    const response = await fetch('http://127.0.0.1:8000/loadfeed', {method:"GET"});
    if (!response.ok)
    {
        console.log(result.error);
        return;
    }

    const result = await response.json();

    const container = document.createElement('ul');
    result.forEach(post => {
        const card = document.createElement('li');
        card.innerHTML = 
        `
            <article class="feed-card" data-id="${post.id}">
                <a class="feed-card-header" href="http://127.0.0.1:8000/profile/${post.userID}">
                    <img src="${((post.userimage === "None") ? "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460__480.png": post.userimage)}"alt="Profile Picture"/>
                    <span>${post.username}</span>
                </a>
                <div class="feed-card-image">
                    <img src="${post.image}">
                </div>
                <div class="feed-card-meta">
                    <div class="interactions">
                        <box-icon name='heart' animation="tada-hover" class="icon"></box-icon>
                        <box-icon name='comment' class="icon"></box-icon>
                    </div>
                    <span>${post.likes} Likes</span>
                </div>
                <div class="feed-card-content">
                    <p>${post.headline}</p>
                </div>
                <div class="feed-card-timestamp">
                    <span>${post.timestamp}</span>
                </div>
            </article>
        `;
        container.append(card);
    })
    contentarea.innerHTML = container.innerHTML;
}


document.addEventListener('DOMContentLoaded', ()=>{
    loadContent();
})
