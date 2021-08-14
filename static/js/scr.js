const buttonLeft = document.querySelector('.left');
const buttonRight = document.querySelector('.right');
const slider = document.querySelector('.slider');


buttonLeft.addEventListener('click', leftLeaf);
buttonRight.addEventListener('click', rightLeaf);

let image = ['img1', 'img2', 'img3', 'img4'];

function leftLeaf() {
    let i = image.indexOf(slider.id);
    if (slider.id === 'img1') {
        slider.id = image[image.length-1];
    } else {
        slider.id = image[i-1];
    }
};


function rightLeaf() {
    let i = image.indexOf(slider.id);
    if (slider.id === image[image.length-1]) {
        slider.id = image[0];
    } else {
        slider.id = image[i+1];
    }
}