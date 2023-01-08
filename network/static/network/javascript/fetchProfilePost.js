fetchProfilePosts = async () =>
{
    const userID = window.location.pathname.split("/").pop();
    const response = await fetch(`http://127.0.0.1:8000/getUserPosts/${userID}`, {method:"GET"})

    if (!response.ok)
    {
        console.log(response.error);
        return;
    }

    const posts = await response.json();
    console.log(posts);
    const container = document.querySelector('#profile-posts');
    container.innerHTML = ``;

    posts.forEach(post => {
        const div = document.createElement('div');
        div.innerHTML = 
        `
            <img src="${post.image}"/>        
        `;
        container.append(div);
    });
}

document.addEventListener('DOMContentLoaded', () => 
    {
        fetchProfilePosts();
    }
);