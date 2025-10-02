const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const cancelButton = document.getElementById("cancelButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        // Use currentTarget to get the button element, not the clicked icon
        let commentId = e.currentTarget.getAttribute("comment_id");
        console.log("Comment ID:", commentId); // Debug log
        
        if (!commentId) {
            console.error("Comment ID is null or undefined");
            return;
        }
        
        let commentElement = document.getElementById(`comment${commentId}`);
        console.log("Comment element:", commentElement); // Debug log
        
        if (commentElement) {
            // Use data attribute for original text, fallback to text extraction
            let commentContent = commentElement.getAttribute('data-original-text') || 
                                commentElement.textContent.trim();
            
            console.log("Comment content:", commentContent); // Debug log
            
            commentText.value = commentContent;
            submitButton.innerHTML = '<i class="fas fa-save me-1"></i>Update';
            submitButton.setAttribute("data-editing-comment-id", commentId);
            
            // Show cancel button
            cancelButton.classList.remove("d-none");
            
            // Set form action to edit endpoint
            const currentUrl = window.location.pathname;
            commentForm.setAttribute("action", `${currentUrl}edit_comment/${commentId}/`);
            
            // Scroll to form for better UX
            commentForm.scrollIntoView({ behavior: 'smooth' });
        } else {
            console.error(`Comment element with ID 'comment${commentId}' not found`);
        }
    });
}

// Handle form submission for comment updates
commentForm.addEventListener("submit", (e) => {
    const editingCommentId = submitButton.getAttribute("data-editing-comment-id");
    
    if (editingCommentId) {
        // Allow form to submit to server for persistence
        const newCommentText = commentText.value.trim();
        
        if (!newCommentText) {
            e.preventDefault();
            showNotification("Comment cannot be empty!", "error");
            return;
        }
        
        // Show loading state
        submitButton.disabled = true;
        submitButton.innerHTML = '<i class="fas fa-spinner fa-spin me-1"></i>Updating...';
        
        // Form will submit to the edit endpoint set in the action attribute
        // The server will handle the update and redirect back
    }
});

// Function to show notifications
function showNotification(message, type) {
    // Create notification element
    const notification = document.createElement("div");
    let alertClass, iconClass;
    
    switch(type) {
        case 'success':
            alertClass = 'alert-success';
            iconClass = 'fa-check-circle';
            break;
        case 'error':
            alertClass = 'alert-danger';
            iconClass = 'fa-exclamation-circle';
            break;
        case 'info':
            alertClass = 'alert-info';
            iconClass = 'fa-info-circle';
            break;
        default:
            alertClass = 'alert-primary';
            iconClass = 'fa-info';
    }
    
    notification.className = `alert ${alertClass} alert-dismissible fade show position-fixed`;
    notification.style.top = "20px";
    notification.style.right = "20px";
    notification.style.zIndex = "9999";
    notification.style.minWidth = "300px";
    
    notification.innerHTML = `
        <i class="fas ${iconClass} me-2"></i>
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    // Add to body
    document.body.appendChild(notification);
    
    // Auto remove after 3 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 3000);
}

// Function to reset comment form
function resetCommentForm() {
    commentText.value = "";
    submitButton.innerHTML = '<i class="fas fa-comment me-1"></i>Post Comment';
    submitButton.removeAttribute("data-editing-comment-id");
    submitButton.disabled = false;
    cancelButton.classList.add("d-none");
    commentForm.removeAttribute("action");
}

// Handle cancel button click
cancelButton.addEventListener("click", () => {
    resetCommentForm();
    showNotification("Edit cancelled", "info");
});

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        // Use currentTarget to get the button element, not the clicked icon
        let commentId = e.currentTarget.getAttribute("comment_id");
        console.log("Delete Comment ID:", commentId); // Debug log
        
        if (!commentId) {
            console.error("Delete: Comment ID is null or undefined");
            return;
        }
        
        const currentUrl = window.location.pathname;
        deleteConfirm.href = `${currentUrl}delete_comment/${commentId}/`;
        deleteModal.show();
    });
}
