// Custom JavaScript for CookBookr

document.addEventListener('DOMContentLoaded', function() {
    console.log('CookBookr loaded successfully!');
    
    // Add smooth scrolling to anchor links
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
    
    // Add loading animation for recipe cards
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
        card.classList.add('fade-in');
    });
    
    // Add console log for debugging
    console.log(`Found ${cards.length} recipe cards on this page`);
});

// Utility function for future AJAX calls
function showNotification(message, type = 'info') {
    // This can be enhanced later for user notifications
    console.log(`${type.toUpperCase()}: ${message}`);
}