function like(username, post_id){
    const likeCount = document.getElementById(`likes-count-${post_id}`);
    const likeButton = document.getElementById(`like-button-${post_id}`);

    fetch(`${username}/like_post/${post_id}`, { method: "POST" })
    .then((res) => res.json())
    .then((data) => {
        likeCount.innerHTML = data["likes"];
        if (data["liked"] === true){
            likeButton.className = "fa-solid fa-thumbs-up";
        }
        else{
            likeButton.className = "fa-regular fa-thumbs-up";
        }
    })
    .catch((e) => alert("Could not like the post."));
}