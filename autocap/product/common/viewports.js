
const createViewport = (label, width, height) => ({
  label,
  width,
  height
});

export const DesktopViewports = {
  SMALL: createViewport('small', 1280, 800),
  DEFAULT: createViewport('default', 1440, 900),
  WIDE: createViewport('wide', 1920, 1080)
};

export const MobileViewports = {
  ANDROID: createViewport('android', 360, 640),
  IPHONE: createViewport('iphone6', 375, 667) // iPhone6/7/8
  // IPHONEX: createViewport('iphonex', 375, 812)
};

export const AllViewportMap = [
  ...Object.values(DesktopViewports),
  ...Object.values(MobileViewports)
].reduce((allMap, viewport) => {
  allMap[viewport.label] = viewport;
  return allMap;
}, {});

/**
 * A handy function for generating viewport list
 *
 * @param device          - if specify device, 'desktop' or 'mobile' or 'both',
 *                          will choose a default viewport for this device.
 *                          ('default' for desktop, 'iphone6' for mobile,
 *                          'default' + 'iphone6' for both)
 *
 * @param typeList        - specify a list of viewport names(comma separated) to
 *                          test. You can use this option to overwrite the default
 *                          viewport list guessed from parameter "device".
 *                         (example of a full list:
 *                         "small,default,wide,android,iphone6")
 */
export const getViewports = (device, typeList = '') => {
  let viewportNames = [DesktopViewports.DEFAULT.label];

  if (typeList) {
    viewportNames = typeList.split(',')
      .filter(name => AllViewportMap[name]);
  } else if (device === 'desktop') {
    viewportNames = [DesktopViewports.DEFAULT.label];
  } else if (device === 'mobile') {
    viewportNames = [MobileViewports.IPHONE.label];
  } else if (device === 'both') {
    viewportNames = [DesktopViewports.DEFAULT.label, MobileViewports.IPHONE.label];
  }

  return viewportNames.map(name => AllViewportMap[name]);
};
