const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.currentTarget.getAttribute("data-comment-id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerHTML = '<i class="fas fa-save me-1"></i>Update';
        
        const currentUrl = window.location.pathname;
        const editUrl = currentUrl + `edit_comment/${commentId}/`;
        commentForm.setAttribute("action", editUrl);
        
        commentForm.scrollIntoView({ behavior: 'smooth' });
    });
}

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.currentTarget.getAttribute("data-comment-id");
        const currentUrl = window.location.pathname;
        const deleteUrl = currentUrl + `delete_comment/${commentId}/`;
        deleteConfirm.href = deleteUrl;
        deleteModal.show();
    });
}
