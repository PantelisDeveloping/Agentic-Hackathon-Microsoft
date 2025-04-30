// DOM Elements
const stateCards = document.querySelectorAll('.state-card');
const interventionCards = document.querySelectorAll('.intervention-card');
const brainWaves = document.querySelector('.brain-waves');
const searchInput = document.querySelector('.search-bar input');
const notificationBtn = document.querySelector('.notification-btn');

// Initialize state values
let focusLevel = 75;
let stressLevel = 30;
let energyLevel = 60;

// Update progress bars
function updateProgressBars() {
    document.querySelector('.state-card.focus .progress').style.width = `${focusLevel}%`;
    document.querySelector('.state-card.stress .progress').style.width = `${stressLevel}%`;
    document.querySelector('.state-card.energy .progress').style.width = `${energyLevel}%`;
}

// Simulate brain waves
function simulateBrainWaves() {
    const canvas = document.createElement('canvas');
    canvas.width = brainWaves.offsetWidth;
    canvas.height = brainWaves.offsetHeight;
    brainWaves.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    let time = 0;
    
    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.beginPath();
        ctx.strokeStyle = '#00f7ff';
        ctx.lineWidth = 2;
        
        for (let x = 0; x < canvas.width; x++) {
            const y = canvas.height / 2 + Math.sin(x * 0.02 + time) * 20;
            if (x === 0) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        }
        
        ctx.stroke();
        time += 0.1;
        requestAnimationFrame(draw);
    }
    
    draw();
}

// Handle intervention actions
function handleInterventionAction(card) {
    const actionBtn = card.querySelector('.action-btn');
    actionBtn.addEventListener('click', () => {
        actionBtn.classList.toggle('pulse');
        // Here you would typically make an API call to update the intervention status
    });
}

// Initialize notifications
function initializeNotifications() {
    let notificationCount = 3;
    const badge = notificationBtn.querySelector('.notification-badge');
    
    notificationBtn.addEventListener('click', () => {
        notificationCount = 0;
        badge.textContent = '';
        badge.style.display = 'none';
    });
}

// Search functionality
function initializeSearch() {
    searchInput.addEventListener('input', (e) => {
        const searchTerm = e.target.value.toLowerCase();
        // Here you would typically make an API call to search for interventions or goals
    });
}

// Update digital twin stats
function updateTwinStats() {
    const stats = [
        { label: 'Cognitive Load', value: 'Medium' },
        { label: 'Neural Activity', value: 'High' },
        { label: 'Memory Retention', value: '85%' },
        { label: 'Learning Rate', value: '1.2x' }
    ];
    
    const statsContainer = document.querySelector('.twin-stats');
    statsContainer.innerHTML = '';
    
    stats.forEach(stat => {
        const statElement = document.createElement('div');
        statElement.className = 'stat';
        statElement.innerHTML = `
            <span class="label">${stat.label}</span>
            <span class="value">${stat.value}</span>
        `;
        statsContainer.appendChild(statElement);
    });
}

// Initialize the application
function init() {
    updateProgressBars();
    simulateBrainWaves();
    interventionCards.forEach(handleInterventionAction);
    initializeNotifications();
    initializeSearch();
    updateTwinStats();
    
    // Simulate real-time updates
    setInterval(() => {
        focusLevel = Math.max(0, Math.min(100, focusLevel + (Math.random() * 2 - 1)));
        stressLevel = Math.max(0, Math.min(100, stressLevel + (Math.random() * 2 - 1)));
        energyLevel = Math.max(0, Math.min(100, energyLevel + (Math.random() * 2 - 1)));
        updateProgressBars();
    }, 5000);
}

// Start the application when the DOM is loaded
document.addEventListener('DOMContentLoaded', init); 