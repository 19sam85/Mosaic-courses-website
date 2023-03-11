import { AboutUs } from '../../components/AboutUs/AboutUs';
import { ChoiseCourse } from '../../components/ChoiseCourse/ChoiseCourse';
import { Gallery } from '../../components/Gallery/Gallery';
import { MainPromo } from '../../components/MainPromo/MainPromo';
import { Reasons } from '../../components/Reasons/Reasons';
import { Slider } from '../../components/Slider/Slider';

export const MaingPage = () => {
  return (
    <>
      <MainPromo />
      <Slider />
      <AboutUs />
      <Reasons />
      <Gallery />
      <ChoiseCourse />
    </>
  );
};
