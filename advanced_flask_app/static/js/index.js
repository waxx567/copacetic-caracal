const nav = document.querySelector(".primary-navigation");
const navToggle = document.querySelector(".mobile-nav-toggle");

navToggle.addEventListener("click", () => {

  const visiblity = nav.getAttribute("data-visible");
  if (visiblity === "false") {
    nav.setAttribute("data-visible", true);
    navToggle.setAttribute("aria-expanded", true);
  } else {
    nav.setAttribute("data-visible", false);
    navToggle.setAttribute("aria-expanded", false);
  }
});

// CODE BELOW IS NOT USED IN THIS APPLICATION
// to use bikes.html instead of seperate pages for each (via app.py)
// Tabs
const tabList = document.querySelector('[role="tablist"]');
const tabs = tabList.querySelectorAll('[role="tab"]');


// Keyboard navigation
// change focus on key input by calling function
tabList.addEventListener('keydown', changeTabFocus);

// allow select
// loop through each tab
tabs.forEach((tab) => {
  // listen for click and call function
  tab.addEventListener('click', changeTabPanel);
});

let tabFocus = 0;
function changeTabFocus(e) {
  const keydownLeft = 37;
  const keydownRight = 39;
  
  // change the tabindex of the current tab to -1
  if (e.keyCode === keydownLeft || e.keyCode === keydownRight) {
    tabs[tabFocus].setAttribute("tabindex", -1);

    // if the right key is pushed, move to the next tab on the right
    if (e.keyCode === keydownRight) {
      tabFocus++;
      // ensure keyboard scrolling does not go out of bounds
      if (tabFocus >= tabs.length) {
        tabFocus = 0;
      }
    // if the left key is pushed, move to the next tab on the left
    } else {
      tabFocus--;
      // ensure keyboard scrolling does not go out of bounds
      if (tabFocus < 0) {
        tabFocus = tabs.length - 1;
      }
    }

    // set selected tabindex to 0
    tabs[tabFocus].setAttribute("tabindex", 0);
    // set the focus on that tab
    tabs[tabFocus].focus();      
  }
};


function changeTabPanel(e) {
  // select target
  const targetTab = e.target;
  // get attribute to select individually
  const targetPanel = targetTab.getAttribute("aria-controls");
  // get image attribute
  const targetImage = targetTab.getAttribute("data-image");

  // identify parent and select
  const tabContainer = targetTab.parentNode;
  // identify parent above that and select
  const mainContainer = tabContainer.parentNode;

  // highlighting the active tab
  tabContainer
    .querySelector('[aria-selected="true"]')
    .setAttribute("aria-selected", false);

  targetTab.setAttribute("aria-selected", true);

  // call function to hide all data before new (selected) data is displayed
  hideContent(mainContainer, '[role="tabpanel"]');
  // call function to remove hidden attribute from selected data (will select all siblings of that) in order to display that data
  showContent(mainContainer, [`#${targetPanel}`]);

  // call function to hide images
  hideContent(mainContainer, 'picture');
  // call function to remove hidden attribute from selected image in order to display that image
  showContent(mainContainer, [`#${targetImage}`])
}

function hideContent(parent, content) {
  parent
    .querySelectorAll(content)
    .forEach((item) => item.setAttribute("hidden", true));
}

function showContent(parent, content) {
  parent.querySelector(content).removeAttribute('hidden');
}