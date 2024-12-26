function deleteNote(noteID){
    fetch('/delete-note', {
        method : 'POST',
        body: JSON.stringify({noteID: noteID})
        }).then((_res) => {
           window.location.href="/"; //reload the window with a get request
        });
    }