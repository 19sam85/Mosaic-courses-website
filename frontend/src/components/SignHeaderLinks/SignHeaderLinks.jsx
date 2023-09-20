import { NavLink } from 'react-router-dom';
import { classNames } from '../../helpers/classNames';
import cls from './SignHeaderLinks.module.scss';

export const SignHeaderLinks = () => {
  const headerLinks = [
    {
      id: '1',
      link: '/sign-in',
      title: 'Войти',
    },
    {
      id: '2',
      link: '/register',
      title: 'Зарегистрироваться',
    },
  ];
  return (
    <>
      {headerLinks.map((link) => (
        <li key={link.id} className={classNames(cls.item, {}, [])}>
          <NavLink
            className={({ isActive }) => `${cls.link} ${cls[`${isActive ? 'active' : ''}`]}`}
            to={link.link}
          >
            {link.title}
          </NavLink>
        </li>
      ))}
    </>
  );
};
