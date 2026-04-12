function showSection(sectionId) {
    //Hide all sections
    const sections = document.querySelectorAll('.section');
    sections.forEach(sec => sec.style.display = 'none');

    //Show selected section
    const selected = document.getElementById(sectionId);
    if (selected) selected.style.display = 'block';
    
}