import React from 'react';
import Breadcrumbs from '@mui/material/Breadcrumbs';
import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';

export default function IconBreadcrumbs({ links, current }) {
  return (
    <div role="presentation">
      <Breadcrumbs aria-label="breadcrumb">
        {links.map((link, index) => (
          <Link
            key={index}
            underline="hover"
            sx={{ display: 'flex', alignItems: 'center' }}
            color="inherit"
            href={link.href}
          >
            {link.icon}
            {link.label}
          </Link>
        ))}
        <Typography
          sx={{ color: 'text.primary', display: 'flex', alignItems: 'center' }}
        >
          {current.icon}
          {current.label}
        </Typography>
      </Breadcrumbs>
    </div>
  );
}