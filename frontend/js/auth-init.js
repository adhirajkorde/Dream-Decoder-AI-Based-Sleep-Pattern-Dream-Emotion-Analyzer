// Authentication initialization and handlers
// Add to the beginning of DOMContentLoaded

// Check authentication
if (!authService.isAuthenticated()) {
    window.location.href = '/login.html';
}

// Display username
const user = authService.getUser();
if (user && document.getElementById('usernameDisplay')) {
    document.getElementById('usernameDisplay').textContent = user.username;
}

// Setup user menu
function setupUserMenu() {
    const menuBtn = document.getElementById('userMenuBtn');
    const menuDropdown = document.getElementById('userMenuDropdown');
    const logoutBtn = document.getElementById('logoutBtn');
    const deleteAccountBtn = document.getElementById('deleteAccountBtn');

    // Toggle dropdown
    if (menuBtn) {
        menuBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            const isVisible = menuDropdown.style.display === 'block';
            menuDropdown.style.display = isVisible ? 'none' : 'block';
        });
    }

    // Close dropdown when clicking outside
    document.addEventListener('click', () => {
        if (menuDropdown) {
            menuDropdown.style.display = 'none';
        }
    });

    // Logout handler
    if (logoutBtn) {
        logoutBtn.addEventListener('click', async () => {
            if (confirm('Are you sure you want to logout?')) {
                try {
                    await authService.logout();
                    window.location.href = '/login.html';
                } catch (error) {
                    console.error('Logout error:', error);
                    // Still redirect even if logout fails
                    authService.clearAuth();
                    window.location.href = '/login.html';
                }
            }
        });
    }

    // Delete account handler
    if (deleteAccountBtn) {
        deleteAccountBtn.addEventListener('click', async () => {
            const confirmed = confirm(
                'WARNING: This will permanently delete your account and ALL your data (dreams, sleep logs, etc.).\n\n' +
                'This action CANNOT be undone!\n\n' +
                'Are you absolutely sure you want to delete your account?'
            );

            if (!confirmed) return;

            // Double confirmation
            const doubleConfirm = confirm(
                'FINAL CONFIRMATION:\n\n' +
                'Type your confirmation by clicking OK to permanently delete your account and all data.'
            );

            if (!doubleConfirm) return;

            try {
                showToast('info', 'Deleting account...');
                await authService.deleteAccount();
                showToast('success', 'Account deleted successfully');
                setTimeout(() => {
                    window.location.href = '/login.html';
                }, 1500);
            } catch (error) {
                showToast('error', 'Failed to delete account: ' + error.message);
            }
        });
    }
}

// Call setupUserMenu after DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupUserMenu);
} else {
    setupUserMenu();
}
