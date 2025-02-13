document.querySelector('.cancel').style.display = 'none';
document.querySelector('.ham').addEventListener("click", () => {
    document.querySelector('.sathvik').classList.toggle('sathvikGo');
    if (document.querySelector('.sathvik').classList.contains('sathvikGo')) {
        document.querySelector('.hun').style.display = 'inline';
        document.querySelector('.cancel').style.display = 'none';

    } else {
        document.querySelector('.hun').style.display = 'none';
        setTimeout(() => {
                   document.querySelector('.cancel').style.display = 'inline';
        }, 400);
     
    }
})