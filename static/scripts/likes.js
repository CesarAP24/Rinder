var likeButton = document.getElementsByClassName("profile-post-like-btn");
    for (var i = 0; i < likeButton.length; i++){
        likeButton[i].addEventListener("click", function(){
            if(this.classList.contains("liked")){
                this.classList.remove("liked")
            }else{
                this.classList.add("liked")
            }
        });
    }