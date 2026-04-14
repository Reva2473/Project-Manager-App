import os
import re

src = "frontend/script.js"
with open(src, "r", encoding="utf-8") as f:
    content = f.read()


















sections = {
    "globals": """
export const API_URL = window.location.hostname.includes('vercel.app') || (window.location.hostname !== '127.0.0.1' && window.location.protocol !== 'file:') ? '/api' : 'http://127.0.0.1:5000/api';

export const state = {
    token: localStorage.getItem('collabtask_token'),
    currentUser: JSON.parse(localStorage.getItem('collabtask_user')),
    isLogin: true,
    activeProjectId: null,
    projectMembers: [],
    userRoleInProject: 'Viewer',
    allProjects: [],
    allTasks: []
};
""",
}
