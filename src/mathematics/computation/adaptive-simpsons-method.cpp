struct simpson {
  double area(
    double l, double r, double fl, double fm, double fr) {
    return (fl + 4 * fm + fr) * (r - l) / 6;
  }
  double solve(double (*f)(double), double l, double m,
    double r, double eps, double fl, double fm, double fr,
    double a) {
    double lm = l + (m - l) / 2, rm = m + (r - m) / 2;
    double flm = f(lm), frm = f(rm);
    double left = area(l, m, fl, flm, fm),
           right = area(m, r, fm, frm, fr);
    if (fabs(left + right - a) <= 15 * eps)
      return left + right + (left + right - a) / 15.0;
    return solve(f, l, lm, m, eps / 2, fl, flm, fm, left) +
      solve(f, m, rm, r, eps / 2, fm, frm, fr, right);
  }
  double solve(
    double (*f)(double), double l, double r, double eps) {
    double m = l + (r - l) / 2;
    double fl = f(l), fm = f(m), fr = f(r);
    return solve(
      f, l, m, r, eps, fl, fm, fr, area(l, r, fl, fm, fr));
  }
}
