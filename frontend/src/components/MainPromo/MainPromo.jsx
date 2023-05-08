import promoImg from '../../images/promo__image_ellipse.png';
import cls from './MainPromo.module.scss';

export const MainPromo = ({ isOpen, setIsOpen }) => {
  return (
    <section className={cls.section}>
      <div className={cls.block}>
        <div className={cls.textContainer}>
          <h1 className={cls.title}>
            Мастер-классы по&nbsp;
            <span className={cls.span}>римской</span>
                        &nbsp;мозаике
          </h1>
          <p className={cls.description}>
            Единственная в Казахстане студия римской мозаики.
          </p>
          <p className={cls.description}>
            Научим создавать античные шедевры на мастер-классах и украсим ваш
            дом оригинальными арт-объектами.
          </p>
          <button onClick={() => setIsOpen(!isOpen)} className={cls.button} type="button">
            Записаться на мастер-класс
          </button>
        </div>
        <div className={cls.wrapper}>
          <img className={cls.image} src={promoImg} alt="Промо картинка" />
          <div className={cls.radius} />
          <div className={cls.rectangle} />
        </div>
      </div>
    </section>
  );
};
