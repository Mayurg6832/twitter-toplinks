/* eslint-disable jsx-a11y/anchor-is-valid */
import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import { Link } from "react-router-dom";
import Typography from "@material-ui/core/Typography";

const useStyles = makeStyles((theme) => ({
  root: {
    "& > * + *": {
      marginLeft: theme.spacing(2),
    },
  },
}));

export default function Links() {
  const classes = useStyles();

  return (
    <Typography className={classes.root}>
      <Link to="/">ALL TWEETS</Link>
      <Link to="/top-user" color="inherit">
        TOP USER LINK
      </Link>
      <Link to="/top-domain" variant="body2">
        TOP DOMAIN
      </Link>
    </Typography>
  );
}
