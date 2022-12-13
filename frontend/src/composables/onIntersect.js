
 export const onIntersect = (
    elementToWatch,
    callback,
    outCallback = () => {},
    once = true,
    options = { threshold: 1.0 }
) => {
    const observer = new IntersectionObserver(([entry]) => {
        if (entry && entry.isIntersecting) {
            callback(entry.target);
            if (once) {
                observer.unobserve(entry.target);
            }
        }

        else {
            outCallback(entry.target);
        }
    }, options);

    observer.observe(elementToWatch);
    return observer;
};
  